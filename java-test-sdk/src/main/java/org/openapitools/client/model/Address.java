/*
 * Samsara API
 * Integrate your data with the Samsara API, customize the Samsara experience, and join a community of developers building with Samsara.
 *
 * The version of the OpenAPI document: 2019-12-12
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.openapitools.client.model.AddressGeofence;
import org.openapitools.client.model.ContactTinyResponse;
import org.openapitools.client.model.TagTinyResponse;

/**
 * An Address object.
 */
@ApiModel(description = "An Address object.")
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2020-01-30T14:01:37.954-08:00[US/Pacific]")
public class Address {
  /**
   * Gets or Sets addressTypes
   */
  @JsonAdapter(AddressTypesEnum.Adapter.class)
  public enum AddressTypesEnum {
    YARD("yard"),
    
    SHORTHAUL("shortHaul");

    private String value;

    AddressTypesEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AddressTypesEnum fromValue(String value) {
      for (AddressTypesEnum b : AddressTypesEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AddressTypesEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AddressTypesEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AddressTypesEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AddressTypesEnum.fromValue(value);
      }
    }
  }

  public static final String SERIALIZED_NAME_ADDRESS_TYPES = "addressTypes";
  @SerializedName(SERIALIZED_NAME_ADDRESS_TYPES)
  private List<AddressTypesEnum> addressTypes = null;

  public static final String SERIALIZED_NAME_CONTACTS = "contacts";
  @SerializedName(SERIALIZED_NAME_CONTACTS)
  private List<ContactTinyResponse> contacts = null;

  public static final String SERIALIZED_NAME_EXTERNAL_IDS = "externalIds";
  @SerializedName(SERIALIZED_NAME_EXTERNAL_IDS)
  private Map<String, String> externalIds = null;

  public static final String SERIALIZED_NAME_FORMATTED_ADDRESS = "formattedAddress";
  @SerializedName(SERIALIZED_NAME_FORMATTED_ADDRESS)
  private String formattedAddress;

  public static final String SERIALIZED_NAME_GEOFENCE = "geofence";
  @SerializedName(SERIALIZED_NAME_GEOFENCE)
  private AddressGeofence geofence;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_LATITUDE = "latitude";
  @SerializedName(SERIALIZED_NAME_LATITUDE)
  private Double latitude;

  public static final String SERIALIZED_NAME_LONGITUDE = "longitude";
  @SerializedName(SERIALIZED_NAME_LONGITUDE)
  private Double longitude;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NOTES = "notes";
  @SerializedName(SERIALIZED_NAME_NOTES)
  private String notes;

  public static final String SERIALIZED_NAME_TAGS = "tags";
  @SerializedName(SERIALIZED_NAME_TAGS)
  private List<TagTinyResponse> tags = null;


  public Address addressTypes(List<AddressTypesEnum> addressTypes) {
    
    this.addressTypes = addressTypes;
    return this;
  }

  public Address addAddressTypesItem(AddressTypesEnum addressTypesItem) {
    if (this.addressTypes == null) {
      this.addressTypes = new ArrayList<AddressTypesEnum>();
    }
    this.addressTypes.add(addressTypesItem);
    return this;
  }

   /**
   * Reporting location type associated with the address (used for ELD reporting purposes).
   * @return addressTypes
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "Reporting location type associated with the address (used for ELD reporting purposes).")

  public List<AddressTypesEnum> getAddressTypes() {
    return addressTypes;
  }


  public void setAddressTypes(List<AddressTypesEnum> addressTypes) {
    this.addressTypes = addressTypes;
  }


  public Address contacts(List<ContactTinyResponse> contacts) {
    
    this.contacts = contacts;
    return this;
  }

  public Address addContactsItem(ContactTinyResponse contactsItem) {
    if (this.contacts == null) {
      this.contacts = new ArrayList<ContactTinyResponse>();
    }
    this.contacts.add(contactsItem);
    return this;
  }

   /**
   * An array of all contact mini-objects that are associated with the given address entry.
   * @return contacts
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "An array of all contact mini-objects that are associated with the given address entry.")

  public List<ContactTinyResponse> getContacts() {
    return contacts;
  }


  public void setContacts(List<ContactTinyResponse> contacts) {
    this.contacts = contacts;
  }


  public Address externalIds(Map<String, String> externalIds) {
    
    this.externalIds = externalIds;
    return this;
  }

  public Address putExternalIdsItem(String key, String externalIdsItem) {
    if (this.externalIds == null) {
      this.externalIds = new HashMap<String, String>();
    }
    this.externalIds.put(key, externalIdsItem);
    return this;
  }

   /**
   * User-defined dictionary of external IDs (key-value pairs). Both the keys and the values of the dictionary are of type string and must be alphanumeric. Each organization can have at most 10 unique external ID keys. To delete an external ID, set its value to null or the empty string (&#x60;\&quot;\&quot;&#x60;). An external ID can be used as a path parameter to retrieve or update that resource.
   * @return externalIds
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "{maintenanceId=250020, payrollId=ABFS18600}", value = "User-defined dictionary of external IDs (key-value pairs). Both the keys and the values of the dictionary are of type string and must be alphanumeric. Each organization can have at most 10 unique external ID keys. To delete an external ID, set its value to null or the empty string (`\"\"`). An external ID can be used as a path parameter to retrieve or update that resource.")

  public Map<String, String> getExternalIds() {
    return externalIds;
  }


  public void setExternalIds(Map<String, String> externalIds) {
    this.externalIds = externalIds;
  }


  public Address formattedAddress(String formattedAddress) {
    
    this.formattedAddress = formattedAddress;
    return this;
  }

   /**
   * The full street address for this address/geofence, as it might be recognized by Google Maps.
   * @return formattedAddress
  **/
  @ApiModelProperty(example = "350 Rhode Island St, San Francisco, CA", required = true, value = "The full street address for this address/geofence, as it might be recognized by Google Maps.")

  public String getFormattedAddress() {
    return formattedAddress;
  }


  public void setFormattedAddress(String formattedAddress) {
    this.formattedAddress = formattedAddress;
  }


  public Address geofence(AddressGeofence geofence) {
    
    this.geofence = geofence;
    return this;
  }

   /**
   * Get geofence
   * @return geofence
  **/
  @ApiModelProperty(required = true, value = "")

  public AddressGeofence getGeofence() {
    return geofence;
  }


  public void setGeofence(AddressGeofence geofence) {
    this.geofence = geofence;
  }


  public Address id(String id) {
    
    this.id = id;
    return this;
  }

   /**
   * ID of the Address.
   * @return id
  **/
  @ApiModelProperty(example = "22408", required = true, value = "ID of the Address.")

  public String getId() {
    return id;
  }


  public void setId(String id) {
    this.id = id;
  }


  public Address latitude(Double latitude) {
    
    this.latitude = latitude;
    return this;
  }

   /**
   * Latitude of the address. Will be geocoded from &#x60;formattedAddress&#x60; if not provided.
   * @return latitude
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "37.765363", value = "Latitude of the address. Will be geocoded from `formattedAddress` if not provided.")

  public Double getLatitude() {
    return latitude;
  }


  public void setLatitude(Double latitude) {
    this.latitude = latitude;
  }


  public Address longitude(Double longitude) {
    
    this.longitude = longitude;
    return this;
  }

   /**
   * Longitude of the address. Will be geocoded from &#x60;formattedAddress&#x60; if not provided.
   * @return longitude
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "37.765363", value = "Longitude of the address. Will be geocoded from `formattedAddress` if not provided.")

  public Double getLongitude() {
    return longitude;
  }


  public void setLongitude(Double longitude) {
    this.longitude = longitude;
  }


  public Address name(String name) {
    
    this.name = name;
    return this;
  }

   /**
   * Name of the address.
   * @return name
  **/
  @ApiModelProperty(example = "Samsara HQ", required = true, value = "Name of the address.")

  public String getName() {
    return name;
  }


  public void setName(String name) {
    this.name = name;
  }


  public Address notes(String notes) {
    
    this.notes = notes;
    return this;
  }

   /**
   * Notes about the address.
   * @return notes
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "Hours of operation: 8am - 6pm; Truck entrance on the Rhode Island street side.", value = "Notes about the address.")

  public String getNotes() {
    return notes;
  }


  public void setNotes(String notes) {
    this.notes = notes;
  }


  public Address tags(List<TagTinyResponse> tags) {
    
    this.tags = tags;
    return this;
  }

  public Address addTagsItem(TagTinyResponse tagsItem) {
    if (this.tags == null) {
      this.tags = new ArrayList<TagTinyResponse>();
    }
    this.tags.add(tagsItem);
    return this;
  }

   /**
   * An array of all tag mini-objects that are associated with the given address entry.
   * @return tags
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "An array of all tag mini-objects that are associated with the given address entry.")

  public List<TagTinyResponse> getTags() {
    return tags;
  }


  public void setTags(List<TagTinyResponse> tags) {
    this.tags = tags;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Address address = (Address) o;
    return Objects.equals(this.addressTypes, address.addressTypes) &&
        Objects.equals(this.contacts, address.contacts) &&
        Objects.equals(this.externalIds, address.externalIds) &&
        Objects.equals(this.formattedAddress, address.formattedAddress) &&
        Objects.equals(this.geofence, address.geofence) &&
        Objects.equals(this.id, address.id) &&
        Objects.equals(this.latitude, address.latitude) &&
        Objects.equals(this.longitude, address.longitude) &&
        Objects.equals(this.name, address.name) &&
        Objects.equals(this.notes, address.notes) &&
        Objects.equals(this.tags, address.tags);
  }

  @Override
  public int hashCode() {
    return Objects.hash(addressTypes, contacts, externalIds, formattedAddress, geofence, id, latitude, longitude, name, notes, tags);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Address {\n");
    sb.append("    addressTypes: ").append(toIndentedString(addressTypes)).append("\n");
    sb.append("    contacts: ").append(toIndentedString(contacts)).append("\n");
    sb.append("    externalIds: ").append(toIndentedString(externalIds)).append("\n");
    sb.append("    formattedAddress: ").append(toIndentedString(formattedAddress)).append("\n");
    sb.append("    geofence: ").append(toIndentedString(geofence)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    latitude: ").append(toIndentedString(latitude)).append("\n");
    sb.append("    longitude: ").append(toIndentedString(longitude)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    notes: ").append(toIndentedString(notes)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

